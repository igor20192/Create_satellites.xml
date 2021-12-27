#! /usr/bin/env python
#  -*- coding: utf-8 -*-


import ftplib
import re
from bs4 import BeautifulSoup
import httpx
import time
from tkinter import messagebox as mb


def beautify_xml(xml_str):
    import xml.dom.minidom

    dom = xml.dom.minidom.parseString(xml_str)
    return dom.toprettyxml()


def download_provider(list_box, logit):
    for continent in ("asia", "europe", "atlantic", "america"):
        try:
            url = f"https://www.lyngsat.com/packages/{continent}.html"
            response = httpx.get(url)
            soup = BeautifulSoup(response.text, "lxml")
            quotes = soup.find("table", {"class": "bigtable"})
            tbody_tag = quotes.contents
            tr_tag = tbody_tag[1]
            td_tag = tr_tag.contents[3]
            for element in td_tag.find_all("font"):
                if element.text[-2:] in ("°E", "°W") and re.findall(
                    "[0-9]", element.text
                ):
                    logit.append(element.text)

            for number, a_tag in enumerate(td_tag.find_all("a")):
                if a_tag.text.__contains__("Freq."):
                    list_box.insert(number, f'{a_tag.get("href")[33:-4]}')
                    print(number)
        except httpx.RequestError as exc:  # An error occurred while requesting
            mb.showerror(
                "HTTPSRequestError!",
                f"An error occurred while requesting {exc.request.url!r}.",
            )
        except httpx.HTTPStatusError as exc:  # Error status_code 4xx,5xx
            mb.showerror(
                "HTTPStatusError !",
                f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.",
            )
    print(logit)


def download(list_box, logit, satellit):

    for i in (
        "asia",
        "europe",
        "atlantic",
        "america",
    ):
        try:
            url = f"https://www.lyngsat.com/{i}.html"
            response = httpx.get(url)
            soup = BeautifulSoup(response.text, "lxml")
            quotes = soup.find("table", {"class": "bigtable"})
            body_tag = quotes.contents
            tr_tag = body_tag[1].contents
            td_tag = tr_tag[3].contents
            td_tr_tag = td_tag[15].contents
            # получаем название спутников
            for strings in td_tr_tag[1].find_all("a"):
                if (
                    strings.contents[0][-1] == "."
                    and strings.get("href")[:5] != "https"
                ):
                    satellit.append(strings.get("href"))

            # получаем позицию спутника
            for i in td_tag[15].find_all("font"):
                if i.text[-2:] in ("°E", "°W") and len(i.text) > 2:
                    logit.append(i.text)
            # наполненине Listbox
            for i in range(len(satellit)):
                list_box.insert(i, logit[i] + "|" + satellit[i][:-5])

        except httpx.RequestError as exc:  # An error occurred while requesting
            mb.showerror(
                "HTTPSRequestError!",
                f"An error occurred while requesting {exc.request.url!r}.",
            )
        except httpx.HTTPStatusError as exc:  # Error status_code 4xx,5xx
            mb.showerror(
                "HTTPStatusError !",
                f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.",
            )


def create_xml(list_box, logit, satellit, progress, rt, button):

    import xml.etree.ElementTree as xml

    x = 20
    root = xml.Element("satellites")  # Создаем XML файл
    root.set("version", "1.0")
    root.set("encoding", "iso-8859-1")
    try:
        for i in list_box.curselection():
            progress["value"] = x  # Progressbar
            rt.update_idletasks()
            time.sleep(0.5)
            x += 20

            # Создаем sat name XML
            if logit[i][-1] == "E":
                position = float(logit[i][:-2]) * 10
            else:
                position = float(logit[i][:-2]) * -10
            sat = xml.Element(
                "sat",
                name=f"{satellit[i][:-5]} ({logit[i][:-4]}{logit[i][-1:]})",
                flags="0",
                position=str(position)[:-2],
            )
            root.append(sat)

            url = f"https://www.lyngsat.com/{satellit[i]}"
            # try:
            response = httpx.get(url)
            soup = BeautifulSoup(response.text, "lxml")
            quotes = soup.find("table", {"class": "bigtable"})
            body_tag = quotes.contents
            tr_tag = body_tag[1].contents
            # td_tag = tr_tag[3].contents
            for i in tr_tag[3].find_all("font"):  # symbol_rate
                txt = i.text
                # print(txt)
                if (
                    re.findall("Rtp", txt)
                    or re.findall("Ltp", txt)
                    or re.findall("Htp", txt)
                    or re.findall("Vtp", txt)
                ):
                    s = txt[2:].find(" ")
                    if txt[2:].__contains__("."):
                        freq = txt[: s - 2].strip()
                    else:

                        # self.frequency.append(txt[:s].strip())
                        freq = txt[:s].strip()

                    if freq[-1] == "L":
                        polarization = "2"
                    elif freq[-1] == "R":
                        polarization = "3"
                    elif freq[-1] == "H":
                        polarization = "0"
                    elif freq[-1] == "V":
                        polarization = "1"
                if (
                    re.findall("V", txt[-1:])
                    or re.findall("H", txt[-1:])
                    or re.findall("R", txt[-1:])
                ):
                    if (
                        re.findall("\d", txt.strip()[:1])
                        and not re.findall("Htp", txt)
                        and not re.findall("Vtp", txt)
                        and not re.findall("Rtp", txt)
                    ):
                        freq = txt.strip()
                        if txt[-1] == "H":
                            polarization = "0"
                        elif txt[-1] == "V":
                            polarization = "1"
                        elif txt[-1] == "R":
                            polarization = "3"

                if re.findall("DVB", txt):
                    if txt not in ("DVB-S", "DVB-S2", "non-DVB"):
                        if re.findall("DVB-S28PSK", txt):
                            s = txt.find("DVB-S28PSK")
                            s += 10
                            s2 = txt.find("/")
                            s2 -= 1
                            # self.symbol_rate.append(txt[s + 10 : s2 - 1])
                            symbol = txt[s:s2]
                            system, modulation = "1", "2"
                            if s2 == -1:
                                s += 10
                                symbol = txt[s:]
                        elif re.findall("DVB-S2X8PSK", txt):
                            # self.symbol_rate.append(txt[11:-5])
                            symbol = txt[11:-5]
                            system, modulation = "1", "2"
                        elif re.findall("DVB-S2XACM", txt):
                            # self.symbol_rate.append(txt[10:-1])
                            symbol = txt[10:-1]
                            system, modulation = "1", "2"

                        elif re.findall("DVB-S2ACM", txt):
                            # self.symbol_rate.append(txt[9:-1])
                            s2 = txt.find("/") - 1
                            symbol = txt[9:s2]
                            system, modulation = "1", "2"

                        elif re.findall("DVB-S216APSK", txt):
                            s = txt.find("DVB-S216APSK") + 12
                            s2 = txt.find("/") - 1
                            # self.symbol_rate.append(txt[s + 12 : s2 - 1])
                            symbol = txt[s:s2]
                            system, modulation = "1", "4"

                        elif re.findall("DVB-S2X16APSK", txt):
                            s2 = txt.find("/") - 1
                            symbol = txt[13:s2]
                            system, modulation = "1", "4"

                        elif re.findall("DVB-S232APSK", txt):
                            s2 = txt.find("/") - 1
                            symbol = txt[12:s2]
                            system, modulation = "1", "4"

                        elif re.findall("DVB-S2X32APSK", txt):
                            s2 = txt.find("/") - 1
                            symbol = txt[13:s2]
                            system, modulation = "1", "4"

                        elif re.findall("DVB-S2QPSK", txt):
                            s2 = txt.find("/")
                            y = s2 - 1
                            # self.symbol_rate.append(txt[10 : s2 - 1])
                            symbol = txt[10:y]
                            system, modulation = "1", "2"
                            if s2 == -1:
                                symbol = txt[10:]

                        elif re.findall("DVB-S8PSK", txt):
                            if txt.__contains__("Turbo"):
                                s2 = txt.find("/") - 1
                                symbol = txt[15:s2]
                                system, modulation = "0", "2"
                            else:
                                s2 = txt.find("/") - 1
                                symbol = txt[9:s2]
                                system, modulation = "0", "2"
                                if s2 == -1:
                                    symbol = txt[9:]

                        elif re.findall("DVB-S", txt):
                            if txt.__contains__("Turbo"):
                                s = txt.find("DVB-S") + 11
                                s2 = txt.find("/") - 1
                                system, modulation = "0", "1"
                                symbol = txt[s:s2]
                            else:
                                s = txt.find("DVB-S")
                                s2 = txt.find("/")
                                system, modulation = "0", "1"
                                z, y = s + 5, s2 - 1
                                if len(txt[z:y]) > 5:
                                    s += 6
                                    s2 -= 1
                                    # self.symbol_rate.append(txt[s+6:s2-1])
                                    symbol = txt[s:s2]

                                else:
                                    # self.symbol_rate.append(txt[s+5:s2-1])
                                    s += 5
                                    s2 -= 1
                                    symbol = txt[s:s2]
                                    if s2 == -1:
                                        symbol = txt[s:]
                        if txt[-3:] == "1/2":
                            fec = "1"
                        elif txt[-3:] == "2/3":
                            fec = "2"
                        elif txt[-3:] == "3/4":
                            fec = "3"
                        elif txt[-3:] == "5/6":
                            fec = "4"
                        elif txt[-3:] == "7/8":
                            fec = "5"
                        else:
                            fec = "0"

                        trasponder = xml.SubElement(
                            sat,
                            "transponder",
                            {
                                "frequency": f"{freq[:-2]}000",
                                "symbol_rate": f"{symbol}000",
                                "polarization": polarization,
                                "fec_inner": fec,
                                "system": system,
                                "modulation": modulation,
                            },
                        )

            # y = list(set(self.frequency))
            # print(sorted(y, key=lambda x: float(x[:-2])))
            # print(self.frequency)
            # print(self.symbol_rate)
        # progress.start()
    except httpx.RequestError as exc:
        mb.showerror(
            "HTTPSRequestError!",
            f"An error occurred while requesting {exc.request.url!r}.",
        )
    except httpx.HTTPStatusError as exc:
        mb.showerror(
            "HTTPStatusError !",
            f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.",
        )

    tree = xml.ElementTree(root)

    with open("New_satellites/satellites.xml", "wb") as fh:
        tree.write(fh)
    with open("New_satellites/satellites.xml", "r") as fin:
        data = fin.read()
    with open("New_satellites/satellites.xml", "wt") as fout:
        fout.write(beautify_xml(data))
    progress.place_forget()
    button.configure(text="DONE!!!")
    button.configure(background="#009900")


def unload_ftp(server_address, login, password, path, button):
    try:
        with ftplib.FTP(server_address, login, password) as ftp, open(
            "New_satellites/satellites.xml", "rb"
        ) as file:
            ftp.storbinary(f"STOR {path}satellites.xml", file)
        button.configure(text="DONE!!!")
        button.configure(background="#009900")

    except TimeoutError:
        mb.showerror("Error", "Invalid ip address!")
    except ftplib.error_perm:
        mb.showerror("Error", "530  Wrong username or password,path file!")
    except AttributeError:
        mb.showerror("Error", "Check your Ftp configuration!")
    except ConnectionRefusedError:
        mb.showerror(
            "Error",
            "The connection is not established because destination computer rejected connection request Check login, ip_address, password",
        )
