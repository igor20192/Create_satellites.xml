#############################################################################
# Generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#  Jun 28, 2021 07:04:52 PM EEST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { \
    satellites_png "./Desktop/create satellites.xml/satellites.png" \
}
vTcl:create_project_images $image_list   ;# In image.tcl


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background #0080c0 
    wm focusmodel $top passive
    wm geometry $top 804x588+301+49
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1370 749
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    button $top.but45 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Download satellite list} 
    vTcl:DefineAlias "$top.but45" "Button1" vTcl:WidgetProc "Toplevel1" 1
    listbox $top.lis46 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -height 342 -width 739 
    $top.lis46 configure -font "TkFixedFont"
    $top.lis46 insert end text
    vTcl:DefineAlias "$top.lis46" "Listbox1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab48 \
        -background #0080c0 -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -text {Login box} 
    vTcl:DefineAlias "$top.lab48" "Label1" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent49 \
        -background #c0c0c0 -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 134 
    vTcl:DefineAlias "$top.ent49" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab50 \
        -background #0080c0 -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -text {Pasword box} 
    vTcl:DefineAlias "$top.lab50" "Label2" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent51 \
        -background #c0c0c0 -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 184 
    vTcl:DefineAlias "$top.ent51" "Entry2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab52 \
        -background #0080c0 -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -text {Ip adress box} 
    vTcl:DefineAlias "$top.lab52" "Label3" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent53 \
        -background #c0c0c0 -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 184 
    vTcl:DefineAlias "$top.ent53" "Entry3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab54 \
        -background #0080c0 -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -text {File satellites.xml} 
    vTcl:DefineAlias "$top.lab54" "Label4" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent55 \
        -background #c0c0c0 -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 184 
    vTcl:DefineAlias "$top.ent55" "Entry4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab56 \
        -background #0080c0 -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -text /etc/tuxbox/ 
    vTcl:DefineAlias "$top.lab56" "Label5" vTcl:WidgetProc "Toplevel1" 1
    button $top.but57 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Create satellites.xml} 
    vTcl:DefineAlias "$top.but57" "Button2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab58 \
        -background #0080c0 -disabledforeground #a3a3a3 -foreground #ff8000 \
        -text {Select satellites from the list and click create satellites.xml } 
    vTcl:DefineAlias "$top.lab58" "Label6" vTcl:WidgetProc "Toplevel1" 1
    button $top.but59 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Load satellites.xml into box} 
    vTcl:DefineAlias "$top.but59" "Button3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab60 \
        -background #0080c0 -disabledforeground #a3a3a3 -foreground #ff8000 \
        -text {doing wait !} 
    vTcl:DefineAlias "$top.lab60" "Label7" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab61 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -image satellites_png -text Label 
    vTcl:DefineAlias "$top.lab61" "Label8" vTcl:WidgetProc "Toplevel1" 1
    button $top.but62 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Multiple 
    vTcl:DefineAlias "$top.but62" "Button4" vTcl:WidgetProc "Toplevel1" 1
    button $top.but63 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Extended 
    vTcl:DefineAlias "$top.but63" "Button5" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab64 \
        -background #0080c0 -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -text {Choice immediately} 
    vTcl:DefineAlias "$top.lab64" "Label9" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab65 \
        -background #0080c0 -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -text {Choice one by one} 
    vTcl:DefineAlias "$top.lab65" "Label10" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but45 \
        -in $top -x 0 -relx 0.41 -y 0 -rely 0.036 -width 137 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lis46 \
        -in $top -x 0 -relx 0.037 -y 0 -rely 0.102 -width 0 -relwidth 0.919 \
        -height 0 -relheight 0.594 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 0 -relx 0.075 -y 0 -rely 0.697 -width 0 -relwidth 0.104 \
        -height 0 -relheight 0.036 -anchor nw -bordermode ignore 
    place $top.ent49 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.731 -width 134 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab50 \
        -in $top -x 0 -relx 0.075 -y 0 -rely 0.765 -width 0 -relwidth 0.107 \
        -height 0 -relheight 0.036 -anchor nw -bordermode ignore 
    place $top.ent51 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.799 -width 184 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab52 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.833 -width 0 -relwidth 0.167 \
        -height 0 -relheight 0.036 -anchor nw -bordermode ignore 
    place $top.ent53 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.867 -width 184 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab54 \
        -in $top -x 0 -relx 0.062 -y 0 -rely 0.901 -width 0 -relwidth 0.179 \
        -height 0 -relheight 0.036 -anchor nw -bordermode ignore 
    place $top.ent55 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.935 -width 184 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab56 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.969 -width 0 -relwidth 0.229 \
        -height 0 -relheight 0.036 -anchor nw -bordermode ignore 
    place $top.but57 \
        -in $top -x 0 -relx 0.435 -y 0 -rely 0.85 -width 117 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab58 \
        -in $top -x 0 -relx 0.286 -y 0 -rely 0.714 -width 0 -relwidth 0.415 \
        -height 0 -relheight 0.036 -anchor nw -bordermode ignore 
    place $top.but59 \
        -in $top -x 0 -relx 0.41 -y 0 -rely 0.952 -width 157 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab60 \
        -in $top -x 0 -relx 0.435 -y 0 -rely 0.901 -width 0 -relwidth 0.142 \
        -height 0 -relheight 0.036 -anchor nw -bordermode ignore 
    place $top.lab61 \
        -in $top -x 0 -relx 0.771 -y 0 -rely 0.748 -width 0 -relwidth 0.167 \
        -height 0 -relheight 0.189 -anchor nw -bordermode ignore 
    place $top.but62 \
        -in $top -x 0 -relx 0.323 -y 0 -rely 0.799 -width 57 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but63 \
        -in $top -x 0 -relx 0.622 -y 0 -rely 0.799 -width 67 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab64 \
        -in $top -x 0 -relx 0.572 -y 0 -rely 0.748 -width 0 -relwidth 0.167 \
        -height 0 -relheight 0.036 -anchor nw -bordermode ignore 
    place $top.lab65 \
        -in $top -x 0 -relx 0.286 -y 0 -rely 0.748 -width 0 -relwidth 0.155 \
        -height 0 -relheight 0.036 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}



set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

