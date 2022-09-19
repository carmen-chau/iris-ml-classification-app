//Retrieving user input first name and last name
firstName = sessionStorage.getItem("userFirstName")
lastName = sessionStorage.getItem("userLastName")

//Displaying user first name and last name in custom "Thank You" message
document.getElementById("firstName").innerText = firstName
document.getElementById("lastName").innerText = lastName
