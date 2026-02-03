export interface Feature {
  title: string;
  support: string;
  details: Array<FeatureDetail>;
  description: string;
  id: string;
  postHorizontal: string;
  postVertical: string;
  postVerticalId: string;
}

interface FeatureDetail {
  title: string;
  support: string;
  href?: string | null;
}
