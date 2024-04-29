describe('test suite 1', () => {
    it('cenario1', () => {
        cy.visit('/');

        cy.get('#nome').type('vinicius')
        cy.get('[type="password"]').type('123')
        cy.get('.submitbtn').click()
    })

    // it('cenario2', () => {
    //     cy.visit('/');
    // })

    // it('cenario3', () => {
    //     cy.visit('/');
    // })
})