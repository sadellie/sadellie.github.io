export type {
    Project
}

interface Project {
    projectName: string
    shortDescription: string
    features: string[]
    stack: string[]
    projectLink: string
    cover: string
    longDescription?: string
}