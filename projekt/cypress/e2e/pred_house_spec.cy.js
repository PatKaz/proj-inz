describe("Test edit profil", ()=>{
    it('edit test', () =>{
        cy.visit("http://127.0.0.1:8000/start");
        cy.get("#log").click({ force: true })
        cy.get("#login").type('test1',{ force: true })
        cy.get("#password").type('test123!@#',{ force: true })
        cy.get(".btn").click({ force: true })
        cy.get("#house").click({ force: true })

        cy.get('#id_area').type(60,{ force: true })
        cy.get('#id_room_num').select('3',{ force: true })
        cy.get('#id_floor').select('Trzecie',{ force: true })
        cy.get('#id_total_floor').type(5,{ force: true })
        cy.get('#id_year_built').type(2020,{ force: true })

        cy.get('#id_dish_washer').select('Tak',{ force: true })
        cy.get('#id_tv_set').select('Tak',{ force: true })
        cy.get('#id_washer').select('Tak',{ force: true })

        cy.get('#id_balcony').select('Tak',{ force: true })
        cy.get('#id_basement').select('Nie',{ force: true })
        cy.get('#id_elevator').select('Tak',{ force: true })
        cy.get('#id_internet').select('Tak',{ force: true })
        cy.get('#id_available_for_students').select('Tak',{ force: true })
        cy.get('#id_two_level').select('Nie',{ force: true })
        cy.get('#id_garden').select('Nie',{ force: true })
        cy.get('#id_district').select('Wola',{ force: true })

        cy.get(".btn").click({ force: true })

    })
  

})