(function () {
    let app = document.getElementById('reg-form');
    let res = [];
    let a = [];

    app.innerHTML += `<h3>Регистрация</h3>`
    let s;
    s = '<form class="regForm" action="" method="post">'

    s += '<label htmlFor="POST-name">username:</label>'
    s += '<input id="POST-name" type="text" name="name"/>'


    s += '<label htmlFor="POST-password">password:</label>'
    s += '<input id="POST-password" type="password" name="password"/>'

    s += '<label htmlFor="cars"> Choose a car: </label>'
    s += '<select id="cars" name="cars">'

    let projectListLoader = new XMLHttpRequest();
    projectListLoader.onreadystatechange = function () {
        if (projectListLoader.readyState == 4) {
            if (projectListLoader.status == 200) {
                let data = JSON.parse(projectListLoader.responseText);
                console.log(data);
                for (let i = 0; i < data.length; i++) {
                    res.push(data[i].name);
                }
                console.log(res);
                a = res;
            }
        }
    }
    s += '</select>'

    s += '<input type="submit" value="Save"/>'
    s += '</form>'

    function projectLoad(){
        projectListLoader.open('GET', 'http://127.0.0.1:8000/api/projects', true);
        projectListLoader.send();
    }
    projectLoad();

    app.innerHTML += s;

})();
