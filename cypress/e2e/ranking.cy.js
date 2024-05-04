describe('test ranking', () => {
    it('cenario1', () => {
        cy.visit('/');

        cy.get('#nome').type('Lucas')
        cy.wait(1500)
        cy.get('[type="password"]').type('12345')
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get(':nth-child(5) > a').click()
        cy.wait(1500)
        cy.get('#avaliado').type('Arthur')
        cy.wait(1500)
        cy.get('[for="rating_4"]').click()
        cy.wait(1500)
        cy.get('.enviar-avaliacao').click()
        cy.wait(1500)
        cy.get(':nth-child(1) > a').click()
        cy.wait(1500)
        cy.get(':nth-child(7) > a').click()
        cy.wait(1500)  
    })

})