describe("Test edit profil", ()=>{
    it('edit test', () =>{
        cy.visit("http://127.0.0.1:8000/login/");
        cy.get("#login").type('test1',{ force: true })
        cy.get("#password").type('test123!@#',{ force: true })
        cy.get(".btn").click({ force: true })

        cy.get("#profil").click({ force: true })
        cy.get(".btn").click({ force: true })
        cy.get('#id_first_name').clear({ force: true }).type('TestFirstName',{ force: true })
        cy.get('#id_last_name').clear({ force: true }).type('TestLastName',{ force: true })
        cy.get(".btn").click({ force: true })
        cy.get("#profil").click({ force: true })
    })
  

})