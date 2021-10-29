const userAgent = navigator.userAgent,
	toggle = document.getElementById("toggler"),
	linksCont = document.getElementById("links"),
	glass = document.getElementById("glass"),
	load = document.getElementById("load"),
	bubbles = document.getElementsByClassName("bubble"),
	dashboard = document.getElementById("dashboard"),
	content = document.getElementsByClassName("content")[0];

if(userAgent.match(/firefox|fxios/i)){
	 alert("Use chrome for best experience.")
}


toggle.addEventListener("click", () => {
	toggle.classList.toggle("clicked");
	linksCont.classList.toggle("expanded");
});

function startAnimation () {
	for (let i = 0; i < bubbles.length; i++) {
		bubbles[i].style.animationPlayState = "running";
	}
}

function displayContent () {
	glass.classList.remove("hide")
	setTimeout(() => {
		dashboard.classList.remove("hide");
		setTimeout(() => {
			content.classList.remove("hide");
			startAnimation();
		}, 100);
	}, 500);
}

window.onload = function () {
	load.classList.add("active");
	setTimeout(() => {
		displayContent();
		load.classList.add("hide");
	}, 5000);
}