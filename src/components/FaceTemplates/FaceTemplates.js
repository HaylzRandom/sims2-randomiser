const templates = ['face', 'brow', 'eyes', 'nose', 'mouth', 'jaw'];

const FaceTemplates = ({ gender }) => {
	const generateFaceTemplates = () => {
		return Math.floor(Math.random() * (27 - 1 + 1)) + 1;
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
