//let userDataStorage = [];
const submittedForm = document.getElementById("contactForm");

submittedForm.addEventListener("submit", function(event){
    const userEmail = document.getElementById("email").value
    const userMessage = document.getElementById("message").value
    if (!(userEmail.includes("@"))){
        alert("You have entered an invalid email!")
        event.preventDefault(); // prevents the form from submitting if there is an invalid email
    }
})


/*
let userDataStorage = [];
document.getElementById("contactForm").addEventListener("submit", function(event){
    event.preventDefault(); //prevents the form from auto-reoloading after submission. auto-reloading would inhibit ability to store user input
    let userData = { //create an object to store user input information
        firstName: document.getElementById("firstName").value,
        lastName: document.getElementById("lastName").value,
        emailAddress: document.getElementById("email").value,
        message: document.getElementById("message").value
    }

    userDataStorage.push(userData); //add element to array
    document.querySelector("form").reset(); //Reset the form for the next entry
    //storing user input in localStorage
    localStorage.setItem("User information", JSON.stringify(userDataStorage));
});


/*
const form = document.getElementById('contactForm');
const log = document.getElementById('log');
form.addEventListener('submit', logSubmit);

function logSubmit(event) {
    //log.textContent = `Form Submitted! Time stamp: ${event.timeStamp}`;
    alert("Hello! I am an alert box!");
    event.preventDefault();
  }
*/