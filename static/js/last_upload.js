var current_time = Date.now();
var content = document.getElementById('last-update');
var upload_date = new Date(content.innerText);

var diff = (current_time - upload_date.getTime())/1000;

if (Math.round(diff/3600) <= 1){
    content.innerText = Math.round(diff/60) + "Minutes ago";
}
else{
    content.innerText = Math.round(diff/3600) + "hours ago"; // Time difference in minutes
}


