import { useRouter } from 'next/router' 
import { useNextSeoProps } from 'nextra-theme-docs'
import { Callout } from 'nextra/components'

export default {
    logo: <span>Topics</span>,
    project: {
      link: 'https://github.com/abhinavmir/ciphertxt',
    },
    useNextSeoProps() {
      return {
        title: 'ツ CipherTxt', 
        description: 'A corpus of exhaustive notes on Cryptography, Secure communication, Network security, Formal Verification, and Structure of Programming Languages.'
      }
    }
  }