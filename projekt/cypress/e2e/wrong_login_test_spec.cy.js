describe("Test login page", ()=>{
    it('test1', () =>{
        cy.visit("http://127.0.0.1:8000/login/");
        cy.get("#login").type('test1',{ force: true })
        cy.get("#password").type('test123a!@#',{ force: true })
        cy.get(".btn").click({ force: true })
        cy.get("#login").type('test1',{ force: true })
        cy.get("#password").type('test123!@#',{ force: true })
        cy.get(".btn").click({ force: true })
    })
  

})







