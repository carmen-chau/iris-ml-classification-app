const submittedForm = document.getElementById("contactForm");

submittedForm.addEventListener("submit", function(event){
    const userEmail = document.getElementById("email").value
    const userFirstName = document.getElementById("firstName").value
    const userLastName = document.getElementById("lastName").value
    if (!(userEmail.includes("@"))){
        alert("You have entered an invalid email!")
        event.preventDefault(); // prevents the form from submitting if there is an invalid email
    }
    //storing user information for the personalized "Thank you for submitting" page
    sessionStorage.setItem("userFirstName", userFirstName)
    sessionStorage.setItem("userLastName", userLastName)
})