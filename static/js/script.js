<script>
    document.getElementById("file-input").addEventListener("change", function() {
        let fileNameText = document.getElementById("file-name");

        if (this.files.length > 0) {
            fileNameText.textContent = this.files[0].name;
        } else {
            fileNameText.textContent = "Insert photo";
        }
    });
</script>