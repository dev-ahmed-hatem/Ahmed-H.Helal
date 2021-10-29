const targets = document.querySelectorAll(".animated");

function checkTargets() {
	targets.forEach((el, key) => {
		if (
			el.offsetTop < document.documentElement.scrollTop + 650 &&
			el.offsetTop > document.documentElement.scrollTop - 500
		) {
			el.classList.add("visible");
		} else {
			el.classList.remove("visible");
		}
	});
}

window.addEventListener("scroll", () => {
	checkTargets();
});
