import React from 'react'
import { graphql } from 'gatsby'

import Layout from '../components/layout'
import { Link } from '../components/link'
import Logo from '../../static/SustainMarsHackathon.svg'

import classes from '../styles/index.module.sass'

export default ({ data }) => {
    const siteMetadata = data.site.siteMetadata
    const chapters = data.allMarkdownRemark.edges.map(({ node }) => ({
        slug: node.fields.slug,
        title: node.frontmatter.title,
        description: node.frontmatter.description,
    }))
    return (
        <Layout isHome>
            <Logo className={classes.logo} aria-label={siteMetadata.title} />

            <section>
                <h1 className={classes.subtitle}> ARE YOU READY TO HACK? </h1>
                <div className={classes.introduction}>
                <p>
                Thanks for joining us Grades 9-12 Canadian students and teachers! This mini-course will help you prepare for the upcoming Callysto hackathon. It's as easy as 3-2-1 <span role="img" aria-label="rocket">🚀</span>   
                </p>
                </div>
            </section>
            
            {chapters.map(({ slug, title, description }) => (
                <section key={slug} className={classes.chapter}>
                    <h2 className={classes.chapterTitle}>
                        <Link hidden to={slug}>
                            {title}
                        </Link>
                    </h2>
                    <p className={classes.chapterDesc}>
                        <Link hidden to={slug}>
                            {description}
                        </Link>
                    </p>
                </section>
            ))}
        </Layout>
    )
}

export const pageQuery = graphql`
    {
        site {
            siteMetadata {
                title
            }
        }
        allMarkdownRemark(
            sort: { fields: [frontmatter___title], order: ASC }
            filter: { frontmatter: { type: { eq: "chapter" } } }
        ) {
            edges {
                node {
                    fields {
                        slug
                    }
                    frontmatter {
                        title
                        description
                    }
                }
            }
        }
    }
`
