document.addEventListener('DOMContentLoaded', () => {
    // 1. Smooth scrolling for TOC links
    const tocLinks = document.querySelectorAll('#toc-nav a');
    
    // Highlight the active TOC item based on scroll position
    const headers = Array.from(document.querySelectorAll('.markdown-body h1, .markdown-body h2, .markdown-body h3'));
    
    // Intersection Observer to track which section is currently visible
    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -80% 0px', // Trigger when header hits top 20%
        threshold: 1.0
    };
    
    // Fallback scroll listener since IntersectionObserver can be tricky with long sections
    window.addEventListener('scroll', () => {
        let currentHeader = '';
        const scrollPosition = document.documentElement.scrollTop || document.body.scrollTop;
        
        // Find the header closest to the top
        for (let i = 0; i < headers.length; i++) {
            const header = headers[i];
            if (header.offsetTop <= scrollPosition + 150) {
                currentHeader = header.id;
            } else {
                break;
            }
        }
        
        if (currentHeader) {
            tocLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${currentHeader}`) {
                    link.classList.add('active');
                    
                    // Auto-scroll TOC sidebar if needed
                    const nav = document.getElementById('toc-nav');
                    const linkRect = link.getBoundingClientRect();
                    const navRect = nav.getBoundingClientRect();
                    
                    if (linkRect.bottom > navRect.bottom || linkRect.top < navRect.top) {
                        link.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }
                }
            });
        }
    });
    
    // 2. Add copy to clipboard buttons on all code blocks
    const preBlocks = document.querySelectorAll('pre');
    
    preBlocks.forEach(pre => {
        // Create the button
        const copyBtn = document.createElement('button');
        copyBtn.innerText = 'Copy';
        copyBtn.className = 'copy-btn';
        
        // Style it programmatically or via CSS
        Object.assign(copyBtn.style, {
            position: 'absolute',
            top: '8px',
            right: '8px',
            background: 'rgba(255, 255, 255, 0.1)',
            border: '1px solid rgba(255, 255, 255, 0.2)',
            color: '#c9d1d9',
            padding: '4px 8px',
            borderRadius: '4px',
            cursor: 'pointer',
            fontSize: '12px',
            fontFamily: 'var(--font-sans)',
            transition: 'all 0.2s',
            opacity: '0',
            visibility: 'hidden'
        });
        
        // Make pre block relative so button positions correctly
        pre.style.position = 'relative';
        
        // Hover effects
        pre.addEventListener('mouseenter', () => {
            copyBtn.style.opacity = '1';
            copyBtn.style.visibility = 'visible';
        });
        
        pre.addEventListener('mouseleave', () => {
            copyBtn.style.opacity = '0';
            copyBtn.style.visibility = 'hidden';
            copyBtn.innerText = 'Copy';
            copyBtn.style.background = 'rgba(255, 255, 255, 0.1)';
        });
        
        copyBtn.addEventListener('mouseenter', () => {
             copyBtn.style.background = 'rgba(255, 255, 255, 0.2)';
        });
        
        copyBtn.addEventListener('mouseleave', () => {
             copyBtn.style.background = 'rgba(255, 255, 255, 0.1)';
        });
        
        // Copy functionality
        copyBtn.addEventListener('click', () => {
            const code = pre.querySelector('code');
            if(code) {
                navigator.clipboard.writeText(code.innerText).then(() => {
                    copyBtn.innerText = 'Copied!';
                    copyBtn.style.background = '#2ea043'; // GitHub green success
                    copyBtn.style.borderColor = '#2ea043';
                    copyBtn.style.color = 'white';
                    
                    setTimeout(() => {
                        copyBtn.innerText = 'Copy';
                        copyBtn.style.background = 'rgba(255, 255, 255, 0.1)';
                        copyBtn.style.borderColor = 'rgba(255, 255, 255, 0.2)';
                    }, 2000);
                });
            }
        });
        
        pre.appendChild(copyBtn);
    });

    // 3. Back to Top Button Logic
    const bttButton = document.getElementById('back-to-top');
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 500) {
            bttButton.style.display = 'block';
        } else {
            bttButton.style.display = 'none';
        }
    });

    bttButton.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});
