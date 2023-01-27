
function getDonorDetails() {
    const donorArray = [];
    const len = localStorage.length-1;
    for(let i=len; i>=0; i--){
      donorArray.push(String(localStorage.getItem(localStorage.key(i))));
    }  
    console.log(donorArray);
  }


const receiverbtn = document.querySelector("#receive_btn");
receiverbtn.addEventListener("click",getDonorDetails,false);


/* receiverPara.innerHTML = `List of Donors : ${donorArray}`; */