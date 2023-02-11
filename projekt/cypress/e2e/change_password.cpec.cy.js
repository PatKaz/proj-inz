describe("Test change password", ()=>{
    it('change password test', () =>{
        cy.visit("http://127.0.0.1:8000/login/");
        cy.get("#login").type('test1',{ force: true })
        cy.get("#password").type('test123!@#',{ force: true })
        cy.get(".btn").click({ force: true })
        cy.get("#profil").click({ force: true })
        cy.get(".btn").click({ force: true })
        cy.get("#ch-pass").click({ force: true })
        cy.get('#id_old_password').type('test123!@#',{ force: true })
        cy.get('#id_new_password1').type('test123!@#',{ force: true })
        cy.get('#id_new_password2').type('test123!@#',{ force: true })
        cy.get(".btn").click({ force: true })
    })
  

})