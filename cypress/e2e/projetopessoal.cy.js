describe('test suite 1', () => {
    it('cenario1', () => {
        cy.visit('/');

        cy.get('#nome').type('User 1')
        cy.get('[type="password"]').type('12345')
        cy.get('.submitbtn').click()
        cy.get(':nth-child(6) > a').click()
        cy.get('#name').type('Projeto Legal')
        cy.get('#description').type('Descrição Legal')
        cy.get('#participants').type('User 1, User 2')
        cy.get('.btn').click()
        cy.get(':nth-child(2) > a').click()
    })

})

