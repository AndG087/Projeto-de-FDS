describe('test suite 1', () => {
    it('cenario1', () => {
        cy.visit('/');

        cy.get('#nome').type('vinicius')
        cy.get('[type="password"]').type('123')
        cy.get('.submitbtn').click()
        cy.get(':nth-child(6) > a').click()
        cy.get('#name').type('Projeto Legal')
        cy.get('#description').type('Descrição Legal')
        cy.get('#participants').type('Lucas e Arthur')
        cy.get('.btn').click()
    })

    // it('cenario2', () => {
    //     cy.visit('/');
    // })

    // it('cenario3', () => {
    //     cy.visit('/');
    // })
})

