// Get the element with id "toggle_header"
let toggleHeaderElement = document.getElementById('toggle_header');

// Add an event listener for the click event
toggleHeaderElement.addEventListener('click', function () {
	let headerElement = document.querySelector('header');

	// Check the current class and toggle between "red" and "green"
	if (headerElement.classList.contains('green')) {
		headerElement.classList.remove('green');
		headerElement.classList.add('red');
	} else {
		headerElement.classList.remove('red');
		headerElement.classList.add('green');
	}
});
