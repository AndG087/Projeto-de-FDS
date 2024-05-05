describe('test avaliação', () => {
    it('cenario1', () => {
        cy.visit('/');

        cy.get('#nome').type('tudo3');
        cy.wait(1500); // Espera 1.5 segundos
        
        cy.get('[type="password"]').type('333');
        cy.wait(1500); // Espera 2 segundos
        
        cy.get('.submitbtn').click();
        cy.wait(1500); // Espera 3 segundos
        
        cy.get(':nth-child(5) > a').click();
        cy.wait(1500); // Espera 1.5 segundos
        
        cy.get('#avaliado').type('Lucas');
        cy.wait(1500); // Espera 1 segundo
        
        cy.get('[for="rating_5"]').click();
        cy.wait(1500); // Espera meio segundo
        
        cy.get('.enviar-avaliacao').click();
        cy.wait(1500)
    });
    it('cenario2', () => {
        cy.visit('/');

        cy.get('#nome').type('tudo3');
        cy.wait(1500); // Espera 1 segundo (1000 milissegundos)
        
        cy.get('[type="password"]').type('333');
        cy.wait(1500); // Espera 2 segundos
        
        cy.get('.submitbtn').click();
        cy.wait(1500); // Espera 3 segundos
        
        cy.get(':nth-child(5) > a').click();
        cy.wait(1500); // Espera 1.5 segundos
        
        cy.get('#avaliado').type('Not exist');
        cy.wait(1500); // Espera 1 segundo
        
        cy.get('[for="rating_3"]').click();
        cy.wait(1500); // Espera meio segundo
        
        cy.get('.enviar-avaliacao').click();
        cy.wait(1500)
    });
});
