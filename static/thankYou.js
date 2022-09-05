//firstName = JSON.stringify(sessionStorage.getItem("userFirstName"))
//lastName = JSON.stringify(sessionStorage.getItem("userLastName"))

firstName = sessionStorage.getItem("userFirstName")
lastName = sessionStorage.getItem("userLastName")

//sessionStorage.getItem("userLastName")

document.getElementById("firstName").innerText = firstName
document.getElementById("lastName").innerText = lastName

/*

document.getElementById("firstName").innerText = (firstName).slice(3,firstName.length)
document.getElementById("firstName").innerText = (lastName).slice(3,lastName.length)

*/