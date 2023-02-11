describe("Test start page", () =>{
    it("add",() =>{
        cy.visit("http://127.0.0.1:8000/start")
        cy.title().should('eq', 'PredApp')
        cy.get()

    })

}

)