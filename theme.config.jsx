import { useRouter } from 'next/router' 
import { useNextSeoProps } from 'nextra-theme-docs'

export default {
    logo: <span>Ciphertxt.com</span>,
    project: {
      link: 'https://github.com/abhinavmir/ciphertxt',
    },
    useNextSeoProps() {
      return {
        title: 'ジ CipherTxt', 
        description: 'A corpus of exhaustive notes on Cryptography, Secure communication, Network security, Formal Verification, and Structure of Programming Languages.'
      }
    }
  }