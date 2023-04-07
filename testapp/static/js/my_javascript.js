function changecolor() {
  console.log("I was clicked!!!");
  document.getElementById("mydiv").style.color = "blue";
  document.getElementById("mydiv").innerHTML =
    "I have just changed completely thanks to the Javascript-Function in the static files folder, which is imported in the base.html. Remember Django renders the templates before they are sent to the brwoser! So for stuff like this, we are in frontend dev...";
}
