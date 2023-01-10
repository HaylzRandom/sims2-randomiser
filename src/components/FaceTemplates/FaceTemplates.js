const templates = ['face', 'brow', 'eyes', 'nose', 'mouth', 'jaw'];

const maleMin = 1;
const maleMax = 55;
const femaleMin = 1;
const femaleMax = 54;

const FaceTemplates = ({ gender }) => {
	const generateFaceTemplates = () => {
		if (gender === 'male') {
			return Math.floor(Math.random() * (maleMax - maleMin + 1)) + maleMin;
		} else {
			return (
				Math.floor(Math.random() * (femaleMax - femaleMin + 1)) + femaleMin
			);
		}
	};

	return (
		<section id='sim-face-templates'>
			<header>
				<h2>Face Templates</h2>
			</header>
			<div className='face-templates'>
				<ul className='template-list'>
					{templates.map((template) => (
						<li key={template}>
							<p>
								<span className='title'>{template}: </span>
								{generateFaceTemplates()} + {generateFaceTemplates()}
							</p>
						</li>
					))}
				</ul>
			</div>
		</section>
	);
};
export default FaceTemplates;
