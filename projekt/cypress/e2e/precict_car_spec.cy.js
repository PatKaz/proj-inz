describe("Test edit profil", ()=>{
    it('edit test', () =>{
        cy.visit("http://127.0.0.1:8000/start");
        cy.get("#log").click({ force: true })
        cy.get("#login").type('test1',{ force: true })
        cy.get("#password").type('test123!@#',{ force: true })
        cy.get(".btn").click({ force: true })
        cy.get("#car").click({ force: true })

        cy.get('#id_mark').select('Audi',{ force: true })
        cy.get('#id_model').select('a4',{ force: true })
        cy.get('#id_year').select('2000',{ force: true })
        cy.get('#id_mileage').type(350000,{ force: true })
        cy.get('#id_fuel').select('Diesel',{ force: true })
        cy.get('#id_vol_engine').type(1900,{ force: true })
        cy.get('#id_province').select('Opolskie',{ force: true })
        cy.get(".btn").click({ force: true })
    })
  

})