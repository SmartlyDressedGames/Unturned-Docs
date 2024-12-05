// Allows for collapsing TOC sections.
// Styling handled by toctree_collapse.css stylesheet.

$(function() {
	let browsing = false; // Is the reader currently on a page included in the TOC?

	// Selects elements from the navigation menu (TOC).
	const headings = document.querySelectorAll(".wy-menu-vertical .caption[role=heading]");
	headings.forEach(caption => {
		const ulist = caption.nextElementSibling;

		// Toggle state when clicked.
		caption.addEventListener("click", () => {
			caption.classList.toggle("toggled");
		});

		// Expand current section be browsed.
		if (ulist.classList.contains("current")) {
			caption.classList.add("toggled");
			browsing = true;
		}
	});

	// If the reader isn't browsing, just expand the first section instead.
	if (browsing == false) {
		headings[0].classList.add("toggled");
	}
});
