describe("Test register profil", ()=>{
    it('register test', () =>{
        cy.visit("http://127.0.0.1:8000/start");
        cy.get('#reg').click({ force: true })
        cy.get('#id_username').type('TestLogin',{ force: true })
        cy.get('#id_first_name').type('TestFirstName',{ force: true })
        cy.get('#id_last_name').type('TestLasttName',{ force: true })
        cy.get('#id_email').type('test@test.com',{ force: true })
        cy.get('#id_password1').type('test123!@#',{ force: true })
        cy.get('#id_password2').type('test123!@#',{ force: true })
        cy.get('#id_captcha_1').
        cy.get('.btn').click({ force: true })
    })
  

})