let fileInput = document.querySelector('#files');
let imagePreview = document.querySelector('.imagePreview');

const handleFilePreview = (e) => {
let files = e.target.files;
let length = files.length;

for(let i = 0; i < length; i++) {
    let image = document.createElement('img');
    // use the DOMstring for source
    image.style = "height: 150px; border: 1px solid #000; margin: 5px;";
    image.src = window.URL.createObjectURL(files[i]);
    imagePreview.appendChild(image);
    }
}

fileInput.addEventListener('change', handleFilePreview);