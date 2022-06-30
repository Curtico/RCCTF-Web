function getCookie (name) {
    // Split cookie string and get all individual name=value pairs in an array
    var cookieArr = document.cookie.split(";");
    
    // Loop through the array elements
    for (var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split("=");
        
        /* Removing whitespace at the beginning of the cookie name
        and compare it with the given string */
        if (name == cookiePair[0].trim()) {
            // Decode the cookie value and return
            return decodeURIComponent(cookiePair[1]);
        }
    }
    
    // Return null if not found
    return null;
}

// Collapsible help dialog
var coll = document.getElementsByClassName("collapsible");
for (let i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = document.getElementById("help-dialog");
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.width = (document.body.clientWidth / 3) + "px";
            content.style.maxHeight = content.scrollHeight + "px";
        } 
    });
}

// Define button listeners
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
            } else {
                console.log("Incorrect flag submitted.");
            }
        })});
    });
}

// Initial cookie check for indicator styles
var indFL = document.getElementById("front-left-motor").getElementsByTagName("p")[0];
var indFR = document.getElementById("front-right-motor").getElementsByTagName("p")[0];
var indRL = document.getElementById("rear-left-motor").getElementsByTagName("p")[0];
var indRR = document.getElementById("rear-right-motor").getElementsByTagName("p")[0];

fetch("/", {method: "POST"}).then(res => res.json()).then(data => {
    console.log(data);
    if (data['front-left-motor'] == "enabled") {
        indFL.style.backgroundColor = "#11bb11";
        indFL.textContent = indFL.textContent.substring(0, indFL.textContent.indexOf(":")) + ": ENABLED";
    }
    if (data['front-right-motor'] == "enabled") {
        indFR.style.backgroundColor = "#11bb11";
        indFR.textContent = indFR.textContent.substring(0, indFR.textContent.indexOf(":")) + ": ENABLED";
    }
    if (data['rear-left-motor'] == "enabled") {
        indRL.style.backgroundColor = "#11bb11";
        indRL.textContent = indRL.textContent.substring(0, indRL.textContent.indexOf(":")) + ": ENABLED";
    }
    if (data['rear-right-motor'] == "enabled") {
        indRR.style.backgroundColor = "#11bb11";
        indRR.textContent = indRR.textContent.substring(0, indRR.textContent.indexOf(":")) + ": ENABLED";
    }
});
