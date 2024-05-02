describe('test suite 1', () => {
    it('cenario1', () => {
        cy.visit('/');

        cy.get('#nome').type('vinicius')
        cy.get('[type="password"]').type('123')
        cy.get('.submitbtn').click()

        cy.get(':nth-child(5) > a').click()
        cy.get('#funcionario_name').type('FÃ¡bio')
        cy.get('[for="rating_5"]').click()
        cy.get('.enviar-avaliacao').click()
    })

    // it('cenario2', () => {
    //     cy.visit('/');
    // })

    // it('cenario3', () => {
    //     cy.visit('/');
    // })
})