

// const fileInput = document.getElementById("file"); //file-input
// const fileNameDiv = document.getElementById("file-name");

// fileInput.addEventListener("change", function() {
//   const fileName = this.value.split("\\").pop();
//   if (fileName) {
//     fileNameDiv.innerHTML = `File chosen: ${fileName}`;
//   } else {
//     fileNameDiv.innerHTML = "";
//   }
// });
const form = document.getElementById('upload-form');
      const fileInput = document.getElementById('file');
      const submitBtn = document.getElementById('submit-btn');
      const previewDiv = document.getElementById('image-preview');

      form.addEventListener('submit', (event) => {
        event.preventDefault();
        const file = fileInput.files[0];
        if (!file) {
          alert('Please select a file');
          return;
        }
        if (!file.type.startsWith('image/')) {
          alert('Please select an image file');
          return;
        }
        const reader = new FileReader();
        reader.onload = (event) => {
          const img = new Image();
          img.onload = () => {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            const maxDimension = 500;
            if (img.width > maxDimension || img.height > maxDimension) {
              const scaleFactor = Math.min(maxDimension / img.width, maxDimension / img.height);
              canvas.width = img.width * scaleFactor;
              canvas.height = img.height * scaleFactor;
            } else {
              canvas.width = img.width;
              canvas.height = img.height;
            }
            ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
            const dataURL = canvas.toDataURL('image/jpeg', 0.8);
            const imgElem = document.createElement('img');
            imgElem.src = dataURL;
            previewDiv.innerHTML = '';
            previewDiv.appendChild(imgElem);
          };
          img.src = event.target.result;
        };
        reader.readAsDataURL(file);
      });