
function setDonorDetails() {
    alert("Details is stored in LocalStorage..");
    const createFrom = document.querySelector(".main__article-create");
    const userName = createFrom.querySelector("#cname").value;
    const userAge = createFrom.querySelector("#age").value;
    const userPhone = createFrom.querySelector("#phone").value;
    const userEmail = createFrom.querySelector("#email").value;
    const userState = createFrom.querySelector("#state").value;
    const userCity = createFrom.querySelector("#city").value;
    const userBloodGroup = createFrom.querySelector("#bloodgroup").value;

    const donorDetails = {
        name : userName,
        age : userAge,
        phoneNo : userPhone,
        email : userEmail,
        state : userState,
        city : userCity,
        bloodGroup : userBloodGroup
    }
    const id = localStorage.length+1;
    localStorage.setItem(`User${id}`,JSON.stringify(donorDetails));
}

const createBtn = document.querySelector("#create_btn");
createBtn.addEventListener("click",setDonorDetails,false);
