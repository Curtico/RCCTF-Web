// Collapsible help dialog
var coll = document.getElementsByClassName("collapsible");

for (let i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = document.getElementById("help-dialog");
        if (content.style.maxHeight){
            content.style.maxHeight = null;
        } else {
            content.style.width = (document.body.clientWidth / 3) + "px";
            content.style.maxHeight = content.scrollHeight + "px";
        } 
    });
}

// POST data for flag authentication
var sendButtons = document.getElementsByClassName("flag-input-button");
for (let i = 0; i < sendButtons.length; i++) {
    sendButtons[i].addEventListener("click", function() {
        var motor = this.parentNode.id;
        var flag = this.parentNode.getElementsByClassName("flag-input-text")[0].value;
        var indicator = this.parentNode.getElementsByTagName("p")[0];
        
        var data = {motor: motor, flag: flag};
        fetch("/flag-auth/", {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
            }).then(res => {res.text().then(text => {
                if (text == "flag_correct") {
                    indicator.style.backgroundColor = "#11bb11";
                    indicator.textContent = indicator.textContent.substring(0, indicator.textContent.indexOf(":")) + ": ENABLED";
                    console.log("Correct flag submitted.");
                }
                else {
                    console.log("Incorrect flag submitted.");
                }
            })});
    });
}
