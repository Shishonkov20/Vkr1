(function () {
    let app = document.getElementById('main');
    app.innerHTML += `<p class="greeting-text">Добро пожаловать, пользователь!</p>`;
    app.innerHTML += `<p>Мои проекты</p>`;
    let projectListLoader = new XMLHttpRequest();
    projectListLoader.onreadystatechange = function () {
        if (projectListLoader.readyState == 4) {
            if (projectListLoader.status == 200) {
                let data = JSON.parse(projectListLoader.responseText);
                console.log(data);
                for (let i = 0; i < data.length; i++) {
                    app.innerHTML += '<p>' + data[i].name + '</p>';
                }
            }
        }
    }
    projectListLoader.open('GET', 'http://127.0.0.1:8000/api/projects', true);
    projectListLoader.send();

})();
