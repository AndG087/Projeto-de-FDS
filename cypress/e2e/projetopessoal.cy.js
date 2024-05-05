describe('test projetos pessoais', () => {
    it('cenario1', () => {
        cy.visit('/');

        cy.get('#nome').type('User 1')
        cy.wait(1500)
        cy.get('[type="password"]').type('12345')
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get(':nth-child(6) > a').click()
        cy.wait(1500)
        cy.get('#name').type('Testando')
        cy.wait(1500)
        cy.get('#description').type('Descrição Legal')
        cy.wait(1500)
        cy.get('#participants').type('User 1, User 2')
        cy.wait(1500)
        cy.get('.btn').click()
        cy.wait(1500)
        cy.get(':nth-child(2) > a').click()
        cy.wait(1500)
    })

})

