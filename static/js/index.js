function upload_image(){
    get_form = document.getElementById("file_upload_form");
    get_form.click()

}

function show_file(){
    // adding and removing class to show and hide some image and forms 
    let show_image= document.getElementById("show_image");
    let upload_image_btn = document.getElementById("upload_image");
    upload_image_btn.classList.remove("Upload-image");
    show_image.classList.remove("hidden_image");
   

    // displaying image to the user 
    val= document.getElementById("file_upload_form");
    parent= document.querySelector("#crop_image");

    // there is a way to acces items of file when change 
    data= document.getElementById("file_upload_form")
    parent.src = URL.createObjectURL(data.files[0]);

    show_image.classList.add("show_image");
    upload_image_btn.classList.add("hide_diagnose_button")

}