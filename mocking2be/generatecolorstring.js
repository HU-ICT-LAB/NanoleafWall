function generatecolorstring(){
    var totalpanels;
    var anidata = "103 ";

    for (totalpanels = 1; totalpanels < 103; totalpanels++) {
        var role1 = totalpanels.toString() + " ";
        var role2 = "1 "
        var role3 = Math.floor(Math.random() * 255).toString() + " ";
        var role4 = Math.floor(Math.random() * 255).toString() + " ";
        var role5 = Math.floor(Math.random() * 255).toString() + " ";
        var role6 = Math.floor(Math.random() * 255).toString() + " ";
        var role7 = "200 ";
        anidata = anidata + role1 + role2 + role3 + role4 + role5 + role6 + role7;
    }
return anidata
}

console.log(anidata);