describe("Test edit profil", ()=>{
    it('edit test', () =>{
        cy.visit("http://127.0.0.1:8000/start");
        cy.get("#log").click({ force: true })
        cy.get("#login").type('test1',{ force: true })
        cy.get("#password").type('test123!@#',{ force: true })
        cy.get(".btn").click({ force: true })
        cy.get("#email").click({ force: true })

        cy.get("#name").type('TestName',{ force: true })
        cy.get(':nth-child(3) > #email').type('TestEmail@email.com',{ force: true })
        cy.get("#phone").type('555666777',{ force: true })
        cy.get('#exampleFormControlTextarea1').type('TestText',{ force: true })
        cy.get(".btn").click({ force: true })

    })
  

})