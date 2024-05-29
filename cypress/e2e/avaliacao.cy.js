Cypress.Commands.add('deleteAllUsers', () => {
    cy.exec('python delete.py', { failOnNonZeroExit: true })
});

describe('test avaliação', () => {
    it('cenario1', () => {
        cy.visit('/');
        cy.exec('python manage.py migrate')
        cy.deleteAllUsers();

        cy.get('[href="/signup/"]').click()
        cy.wait(1500)
        cy.get('#nome').type("Lucas")
        cy.wait(1500)
        cy.get('#email').type("l@gmail.com")
        cy.wait(1500)
        cy.get('[type="password"]').type("12345")
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get('a').click()
        cy.wait(1500)
        cy.get('#nome').type("tudo3")
        cy.wait(1500)
        cy.get('#email').type("tudo@gmail.com")
        cy.wait(1500)
        cy.get('[type="password"]').type("333")
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get('#nome').type('tudo3');
        cy.wait(1500); // Espera 1.5 segundos
        
        cy.get('[type="password"]').type('333');
        cy.wait(1500); // Espera 2 segundos
        
        cy.get('.submitbtn').click();
        cy.wait(1500); // Espera 3 segundos
        
        cy.get(':nth-child(6) > a').click()
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
        cy.exec('python manage.py migrate')
        cy.deleteAllUsers();
        
        cy.get('[href="/signup/"]').click()
        cy.wait(1500)
        cy.get('#nome').type("Arthur")
        cy.wait(1500)
        cy.get('#email').type("A@gmail.com")
        cy.wait(1500)
        cy.get('[type="password"]').type("12345")
        cy.wait(1500)
        cy.get('.submitbtn').click()
        cy.wait(1500)
        cy.get('#nome').type('Arthur');
        cy.wait(1500); // Espera 1 segundo (1000 milissegundos)
        
        cy.get('[type="password"]').type('12345');
        cy.wait(1500); // Espera 2 segundos
        
        cy.get('.submitbtn').click();
        cy.wait(1500); // Espera 3 segundos
        
        cy.get(':nth-child(6) > a').click();
        cy.wait(1500); // Espera 1.5 segundos
        
        cy.get('#avaliado').type('Not exist');
        cy.wait(1500); // Espera 1 segundo
        
        cy.get('[for="rating_3"]').click();
        cy.wait(1500); // Espera meio segundo
        
        cy.get('.enviar-avaliacao').click();
        cy.wait(1500)
    });
});
