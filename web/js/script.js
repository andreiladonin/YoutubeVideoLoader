async function download_video () {
    document.querySelector('.result').innerHTML = "Загрузка началась";
    const url_video = document.querySelector('#link_video').value;
    const title = document.querySelector('#title_video').value;
    const result = await eel.download_video(url_video, title)();
    return result
}

document.querySelector('#btn_download').addEventListener("click", async function() {
    const result = await download_video();
    document.querySelector('.result').innerHTML = result;
})

