class ActionSpace:
    def __init__(self):
        self.public_actions = {
            "express_friendliness": {
                "description": """
                Expressing friendliness does not directly alter the state transition matrix but sets the stage for potential cooperation in the following rounds. This action is pivotal for civilizations considering to initiate cooperation, as it demonstrates peaceful intentions. Note: Actual matrix adjustments depend on subsequent actions and interactions.
                """,
                "matrix_impact": "No direct impact on state transition matrix for the current round."
            },
            "initiate_cooperation": {
                "description": """
                Initiating cooperation increases the diagonal sum of the state transition matrix to 6.5, representing a boost in overall development due to synergies. However, it necessitates reducing the military capability coefficient below 1.2, making the civilization potentially more vulnerable to attacks.
                """,
                "matrix_impact": "Increase diagonal sum to 6.5; military capability coefficient must be below 1.2."
            },

            "launch_annihilation_war": {
                "description": """
                Launching an annihilation war is an extreme measure taken with the intent to completely eradicate another civilization. Success requires the aggressor's military capability to be at least twice that of the target. If successful, the aggressor gains half of the target's resources (excluding military) for that round. However, engaging in annihilation war exposes the aggressor to the entire galaxy, significantly reducing military strength due to the Lanchester's Law and potentially inviting collective retaliation.
                """,
                "matrix_impact": "No "
            },

            "reject_cooperation": """
            Rejecting cooperation is a decision to decline an offer or opportunity for joint development with another civilization. This action might be taken due to strategic considerations, lack of trust, or incompatible objectives. While it may preserve autonomy and prevent potential vulnerabilities, it also foregoes the benefits that cooperation could bring.
            """
        }

        self.private_actions = {
            "description": """
                War mobilization allows a significant increase in the military capability coefficient beyond 1.5, up to a maximum of 2.0, while keeping the total diagonal sum at 6. This action enables rapid military strengthening but requires sacrifices in other areas to maintain balance.
                """,
                "matrix_impact": "Military capability coefficient can exceed 1.5 up to 2.0; total diagonal sum remains at 6."
        }

    def get_action_description(self, action_name):
        if action_name in self.public_actions:
            return self.public_actions[action_name]
        elif action_name in self.private_actions:
            return self.private_actions[action_name]
        else:
            return "Unknown action"

