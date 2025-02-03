class Header extends HTMLElement {
    constructor() {
        super();
        this.innerHTML += `<h1 class="my-header-title">ООО "Управление проектами"</h1>`;
        this.innerHTML += `<p class="reg-link"><a href="registration.html">Регистрация</a></p>`;
    }
}

customElements.define("my-header", Header);