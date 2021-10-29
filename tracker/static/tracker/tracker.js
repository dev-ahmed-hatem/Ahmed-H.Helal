var child = document.getElementsByClassName("child-cont"),
	titles = document.getElementsByClassName("cont-title"),
	mainCont = document.getElementById("main-container"),
	mainHeader = document.getElementById("main-header"),
	i;

for (i = 0; i < child.length; i++) {
	child[i].addEventListener("click", function () {
		this.classList.add("cont-active");
		mainHeader.innerHTML = document
			.querySelector(".cont-active .cont-title")
			.getAttribute("data-title");
		let newTitle = document
			.querySelector(".cont-active .cont-title")
			.getAttribute("data-title");
		mainHeader.setAttribute("data-title", newTitle);
		mainCont.classList.add("main-active");
		setTimeout(function () {
			document
				.querySelector(".cont-active .content .cls-button")
				.classList.add("cls-button-active");
		}, 1400);
	});
}

document.querySelectorAll(".cls-button").forEach(function (button) {
	button.addEventListener("click", function (e) {
		e.stopPropagation();
		button.classList.remove("cls-button-active");
		document.querySelector(".cont-active").classList.remove("cont-active");
		document.querySelector(".main-active").classList.remove("main-active");
		mainHeader.innerHTML = "MAIN MENU";
		mainHeader.setAttribute("data-title", "MAIN MENU");
	});
});
