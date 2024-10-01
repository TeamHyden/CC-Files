function generateRandomNumber() {
    let randomNumber = Math.floor(Math.random() * 90000) + 10000;
    return randomNumber.toString();
  }

var submit_btn = document.getElementsByClassName('submit-btn');

submit_btn.addEventListner('submit',()=>{

    alert('ehllo')
    generateRandomNumber();


});

