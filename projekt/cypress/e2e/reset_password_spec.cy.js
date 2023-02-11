describe("Test edit profil", ()=>{
    it('edit test', () =>{
        cy.visit("http://127.0.0.1:8000/start");
        cy.get("#log").click({ force: true })
        cy.get(".forget-link").click({ force: true })
        cy.get('#id_email').type('patryk.kazmierczak92@gmail.com' ,{ force: true })
        cy.get(".btn").click({ force: true })

        cy.visit("http://127.0.0.1:8000/reset/Mg/birfh5-a471e595fbfb95e44b5975309645deb1/")
        cy.get('#id_new_password1').type('test123!@#' ,{ force: true })
        cy.get('#id_new_password2').type('test123!@#' ,{ force: true })
        cy.get('.btn').click({ force: true })
    })
  

})