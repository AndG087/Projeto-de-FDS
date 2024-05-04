describe('test pesquisa', () => {
    it('cenario1', () => {
        cy.visit('/');

        cy.get('#nome').type('Lucas')
        cy.wait(1500)
        cy.get('[type="password"]').type('12345')
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get(':nth-child(8) > a').click()
        cy.wait(1500)
        cy.get('input').type("Projeto Legal")
        cy.wait(1500)
        cy.get('button').click()
        cy.wait(1500)
    })
    it('cenario2', () => {
        cy.visit('/');

        cy.get('#nome').type('Lucas')
        cy.wait(1500)
        cy.get('[type="password"]').type('12345')
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get(':nth-child(8) > a').click()
        cy.wait(1500)
        cy.get('input').type("Arthur")
        cy.wait(1500)
        cy.get('button').click()
        cy.wait(1500)
    })
    it('cenario3', () => {
        cy.visit('/');

        cy.get('#nome').type('Lucas')
        cy.wait(1500)
        cy.get('[type="password"]').type('12345')
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get(':nth-child(8) > a').click()
        cy.wait(1500)
        cy.get('input').type("Cesar")
        cy.wait(1500)
        cy.get('button').click()
        cy.wait(1500)
    })

})