# ShowerRefiner

This LArLite repository is designed to contain modules which refine shower quantities after shower reconstruction has been run. This generally involves the comparison of the reconstructed shower profile itself (ie. the cone) with the initial hits and clusters, and resolving any tensions between the two.

## ShowerHitRefiner

This module is designed to be run after LArLite ShowerReco3D. It searches for any shower hits that have been missed during the clustering stage, and then reintegrates them into the shower.

This module requires reconstructed shower objects, as well as the clusters and hits associated with this shower. It will loop over all hits in the event, and identify any which are not associated with any shower clusters. It will then compare these unclustered hits with the shower profiles of all showers in the event, and see if it falls inside any cone. If an unclustered hit is located within exactly one shower, it is reintegrated into the appropriate shower.

A new association from cluster => hit is assigned, as well as a new hit data product, which is identical in content to the original hit data product, but is created regardless to prevent any potential conflicts.

Issues with this module:
- Any hits that are clustered into some object other than the shower object with user-specified producer name, the module will treat this hit as unclustered. This may result in track-associated hits being erroneously considered, and so should be fixed.
- Currently, any unclustered hit that falls within the profile of multiple showers is ignored. A decision-making function should be implemented which can discern (maybe based on things like proximity to shower axis) which of the showers the hit belongs to.
